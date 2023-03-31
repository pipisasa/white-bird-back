from django.contrib import admin
from django.http import HttpResponse
from django.utils.encoding import escape_uri_path

from uuid import uuid4

from openpyxl import Workbook

from apps.reqs.models import RequestModel


class RequestModelAdmin(admin.ModelAdmin):
    actions = ("export_to_excel",)
    list_filter = (
        "country",
        "city",
        "role",
        "date_created",
        "full_name",
        "email",
        "phone_number",
    )

    def export_to_excel(self, request, queryset):
        workbook = Workbook()
        worksheet = workbook.active

        worksheet.append(
            (
                "ФИО",
                "электронная почта",
                "номер телефона",
                "страна",
                "роль",
                "дата заявки",
            )
        )

        for obj in queryset:
            row = (
                obj.full_name,
                obj.email,
                obj.phone_number,
                obj.country,
                obj.role,
                obj.date_created,
            )
            worksheet.append(row)

        response = HttpResponse(
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        response["Content-Disposition"] = "attachment; filename*=UTF-8''{}".format(
            escape_uri_path(f"заявки_{uuid4()}.xlsx")
        )
        workbook.save(response)
        return response

    export_to_excel.short_description = "Экспортировать данные заявок в Excel"


admin.site.register(RequestModel, RequestModelAdmin)
