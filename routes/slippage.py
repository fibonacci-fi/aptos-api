from flask import Blueprint, jsonify, request
from models.aptos_transactions import AptosTransactions
from extensions import db
import logging
bp = Blueprint('slippage', __name__)
from sqlalchemy import func, Integer, Float, and_ 
from datetime import datetime, timedelta, timezone
from statistics import median  # Import the median functio
# Set up a logger for error handling
logger = logging.getLogger(__name__)



@bp.route('/api/slippage', methods=['GET'])
def get_slippage():
    """
    Retrieve slippage values for the Aptos/USDC pair from the aptos_transactions table with time binning.

    Query Parameters:
        range (str): The time range for the query. Can be 'hour', 'week', or 'month'.
                     Defaults to 'hour' if not provided or invalid.

    Returns:
        JSON: A dictionary with the pair ('apt-usdc') and binned slippage data.
    """
    try:
        # Get and validate the 'range' parameter, default to 'hour' if invalid
        time_range = request.args.get('range', 'hour').lower()
        if time_range not in ['hour', 'week', 'month']:
            time_range = 'hour'

        # Calculate the start time and define binning intervals
        now = datetime.now(timezone.utc)
        if time_range == 'hour':
            start_time = now - timedelta(hours=1)
            bin_interval = 5  # 5-minute bins
        elif time_range == 'week':
            start_time = now - timedelta(weeks=1)
            bin_interval = 5  # 5-minute bins
        elif time_range == 'month':
            start_time = now - timedelta(days=30)
            bin_interval = 30  # 30-minute bins

        # Define the token pair condition
        token_condition = db.or_(
            db.and_(
                AptosTransactions.coin1 == '0x1::aptos_coin::AptosCoin',
                AptosTransactions.coin2 == '0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDC'
            ),
            db.and_(
                AptosTransactions.coin1 == '0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDC',
                AptosTransactions.coin2 == '0x1::aptos_coin::AptosCoin'
            )
        )

        # Query to get transactions within the specified range
        query = db.session.query(
            AptosTransactions.timestamp,
            AptosTransactions.slippage
        ).filter(
            AptosTransactions.timestamp >= start_time,
            token_condition
        )

        # Fetch results and apply binning
        transactions = query.order_by(AptosTransactions.timestamp.asc()).all()

        # Group transactions into bins
        bins = {}
        for txn in transactions:
            # Calculate the bin key (start of the interval)
            bin_start = txn.timestamp.replace(
                minute=(txn.timestamp.minute // bin_interval) * bin_interval,
                second=0,
                microsecond=0
            )
            if bin_start not in bins:
                bins[bin_start] = []
            bins[bin_start].append(txn.slippage)

        # Calculate the median slippage for each bin
        binned_data = [
            {
                "timestamp": bin_start.isoformat(),
                "slippage": round(float(median(bins[bin_start])), 8)  # Round for readability
            }
            for bin_start in sorted(bins.keys())
        ]

        # Return the response with the pair and binned data
        return jsonify({"pair": "apt-usdc", "data": binned_data})

    except Exception as e:
        logger.error(f"An error occurred while retrieving slippage data: {str(e)}", exc_info=True)
        return jsonify({"error": "An error occurred while processing the request"}), 500
