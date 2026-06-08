from django.db import connection
from django.http import JsonResponse


def backend_home(request):
    return JsonResponse(
        {
            "service": "LeafAI backend",
            "status": "ok",
            "health": "/api/health/",
            "admin": "/admin/",
        }
    )


def health_check(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("select 1")
            cursor.fetchone()
    except Exception:
        return JsonResponse(
            {"status": "error", "database": "unavailable"},
            status=503,
        )

    return JsonResponse({"status": "ok", "database": "ok"})
