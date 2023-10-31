from datetime import datetime
from uuid import UUID
import uuid

from fastapi import HTTPException
from starlette.responses import Response
from starlette import status
from http import HTTPStatus

from ..app import app
from ..api.schemas import CreateOrderSchema, GetOrderSchema, GetOrdersSchema, Status

ORDERS = []

orders = {
    'id': 'ff0f1355-e821-4178-9567-550dec27a373',
    'status': 'delivered',
    'created': datetime.utcnow(),
    'order': [
        {
            'product': 'cappuccino',
            'size': 'medium',
            'quantity': 1
        }
    ]
}

@app.get('/orders', response_model=GetOrdersSchema)
def get_orders():
    return {'orders': ORDERS}

@app.post('/orders', status_code=status.HTTP_201_CREATED, response_model=GetOrdersSchema)
def create_order(order_detail: CreateOrderSchema):
    order = order_detail.dict()
    order['id'] = uuid.uuid4()
    order['created'] = datetime.utcnow()
    order['status'] = 'created'
    ORDERS.append(order)
    return order

@app.get('/orders/{order_id}')
def get_order(order_id: UUID):
    # 注文をIDで検索するために、ORDERS リストを順番に処理してIDをチェック
    for order in ORDERS:
        if order['id'] == order_id:
            return order
    # 注文が見つからない場合は、 status_code を 404 に設定した上で HTTPException を生成し、404レスポンスを返す
    raise HTTPException(
        status_code=404,
        detail=f'Order with ID {order_id} not found'
    )

@app.put('orders/{order_id}')
def update_order(order_id: UUID, order_details: CreateOrderSchema):
    for order in ORDERS:
        if order['id'] == order_id:
            order.update(order_details.dict())
            return order
    raise HTTPException(
        status_code=404,
        detail=f'Order with ID {order_id} not found'
    )

@app.delete(
    '/orders/{order_id}', 
    status_code=status.HTTP_204_NO_CONTENT,
    response_class=Response # response_class を指定することで、通常 JSON オブジェクトが返される設定を上書きできる。
)
def delete_order(order_id: UUID):
    for index, order in enumerate(ORDERS):
        if order['id'] == order_id:
            ORDERS.pop(index)
            return Response(status_code=HTTPStatus.NO_CONTENT.value)
    raise HTTPException(
        status_code=404,
        detail=f"Order with ID {order_id} not found."
    )

@app.post('/orders/{order_id}/cancel')
def cancel_order(order_id: UUID):
    for order in ORDERS:
        if order['id'] == order_id:
            order['status'] == Status.cancelled.value
            return order
    raise HTTPException(
        status_code=404,
        detail=f"Order with ID {order_id} not found."
    )

@app.post('/orders/{order_id}/pay')
def pay_order(order_id: UUID):
    for order in ORDERS:
        if order['id'] == order_id:
            order['status'] = Status.progress.value
            return order
    raise HTTPException(
        status_code=404,
        detail=f"Order with ID {order_id} not found."
    )