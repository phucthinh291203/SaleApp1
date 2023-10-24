def load_categories():
    return [{
        'id':1,
        'name': 'Mobile'
    },{
        'id': 1,
        'name': 'Tablet'
    }]

def load_products(kw=None):
    products = [{
        'id': 1,
        'name': 'iPhone',
        'price': '50000000',
        'image':'https://media-ik.croma.com/prod/https://media.croma.com/image/upload/v1694674445/Croma%20Assets/Communication/Mobiles/Images/300822_0_on2t4l.png?tr=w-600'
    }, {
        'id': 2,
        'name': 'iPad',
        'price': '50000000',
        'image':'https://media-ik.croma.com/prod/https://media.croma.com/image/upload/v1694674445/Croma%20Assets/Communication/Mobiles/Images/300822_0_on2t4l.png?tr=w-600'
    } ,{
        'id': 3,
        'name': 'iPhone',
        'price': '50000000',
        'image':'https://media-ik.croma.com/prod/https://media.croma.com/image/upload/v1694674445/Croma%20Assets/Communication/Mobiles/Images/300822_0_on2t4l.png?tr=w-600'
    },{
        'id': 4,
        'name': 'iPhone',
        'price': '50000000',
        'image':'https://media-ik.croma.com/prod/https://media.croma.com/image/upload/v1694674445/Croma%20Assets/Communication/Mobiles/Images/300822_0_on2t4l.png?tr=w-600'
    },{
        'id': 5,
        'name': 'iPhone',
        'price': '50000000',
        'image':'https://media-ik.croma.com/prod/https://media.croma.com/image/upload/v1694674445/Croma%20Assets/Communication/Mobiles/Images/300822_0_on2t4l.png?tr=w-600'
    },{
        'id': 6,
        'name': 'iPhone',
        'price': '50000000',
        'image':'https://media-ik.croma.com/prod/https://media.croma.com/image/upload/v1694674445/Croma%20Assets/Communication/Mobiles/Images/300822_0_on2t4l.png?tr=w-600'
    }]
    if kw:
        products =[p for p in products if p['name'].find(kw) >=0]
    return products