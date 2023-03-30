from uuid import uuid4

from openpyxl import Workbook

from django.http import HttpResponse
from django.utils.encoding import escape_uri_path

from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

from apps.reqs.models import RequestModel
from apps.reqs.serializers import RequestModelSerializer


class RequestModelAPIView(CreateAPIView):
    queryset = RequestModel.objects.all()
    serializer_class = RequestModelSerializer


class RequestModelExportView(APIView):
    def get(self, request):
        # Получаем все объекты модели
        queryset = RequestModel.objects.all()
        # Создаем новый workbook
        workbook = Workbook()
        # Создаем новый worksheet
        worksheet = workbook.active
        # Добавляем названия столбцов в первую строку
        worksheet.append(["ФИО", "электронная почта", "номер телефона", "страна", "роль", "дата заявки"])
        # Добавляем данные из queryset в worksheet
        for obj in queryset:
            row = [obj.full_name, obj.email, obj.phone_number, obj.country, obj.role, obj.date_created]
            worksheet.append(row)
        # Создаем HTTP response с xlsx файлом во вложении
        response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response["Content-Disposition"] = 'attachment; filename*=UTF-8\'\'{}'.format(
            escape_uri_path(f"заявки_{uuid4()}.xlsx")
        )
        workbook.save(response)
        return response

