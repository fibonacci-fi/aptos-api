from extensions import db

class AptosTransactions(db.Model):
    __tablename__ = 'aptos_transactions'

    id = db.Column(db.Integer, primary_key=True)
    version = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime(timezone=True), nullable=False)
    pool_address = db.Column(db.String, nullable=False)
    coin1 = db.Column(db.String, nullable=False)
    coin2 = db.Column(db.String, nullable=False)
    provider = db.Column(db.String, nullable=True)
    volume = db.Column(db.Numeric, nullable=True)
    delta_x = db.Column(db.Numeric, nullable=True)
    price_x = db.Column(db.Numeric, nullable=True)
    fees = db.Column(db.Numeric, nullable=True)
    tvl = db.Column(db.Numeric, nullable=True)
    slippage = db.Column(db.Numeric, nullable=True)
    decimal_x = db.Column(db.Integer, nullable=True)
    delta_y = db.Column(db.Numeric, nullable=True)
    price_y = db.Column(db.Numeric, nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), nullable=True)
    pool_name = db.Column(db.String, nullable=True)

    def to_dict(self):
        return {
            'id': self.id or 0,
            'version': self.version or 0,
            'timestamp': self.timestamp.isoformat() if self.timestamp else '',
            'pool_address': self.pool_address or '',
            'coin1': self.coin1 or '',
            'coin2': self.coin2 or '',
            'provider': self.provider or '',
            'volume': float(self.volume or 0.0),
            'delta_x': float(self.delta_x or 0.0),
            'price_x': float(self.price_x or 0.0),
            'fees': float(self.fees or 0.0),
            'tvl': float(self.tvl or 0.0),
            'slippage': float(self.slippage or 0.0),
            'decimal_x': self.decimal_x or 0,
            'delta_y': float(self.delta_y or 0.0),
            'price_y': float(self.price_y or 0.0),
            'created_at': self.created_at.isoformat() if self.created_at else '',
            'pool_name': self.pool_name or '',
        }
