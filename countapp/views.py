from django.http import JsonResponse
from django.db import connection


# Create your views here.


def block_cnt(request):
    c = connection.cursor()
    sql = """
    SELECT sum(file_size) filesize, month(create_time) month_
    FROM t_file
    GROUP BY month(create_time)
    ORDER BY month_
    """
    c.execute(sql)
    data = dict(c.fetchall())

    return JsonResponse({
        'data': {
            'month': [str(item) + "月" for item in data.values()],
            'values': [round(item / 1024, 2) for item in data.keys()],
            'x_title': '2020年',
            'y_title': '空间大小(K)'
        }
    })


def user_cnt(request):
    c = connection.cursor()
    sql = """
    SELECT count(user_id) cnt_, month(create_time) month_
    FROM t_user
    GROUP BY month(create_time)
    ORDER BY month_
    """
    c.execute(sql)
    data = dict(c.fetchall())
    print(data)

    return JsonResponse({
        'data': {
            'month': [str(item) + "月" for item in data.values()],
            'values': [
                {
                    'name': str(v)+"月",
                    'value': k
                }
                for k, v in data.items()
            ]
        },
        'x_title': '2020年',
        'y_title': '用户量'
    })
