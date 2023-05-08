import json
from datetime import datetime
from django_pandas.io import read_frame
from rest_framework import response, status
from rest_framework.views import APIView

from hrapi.models import Professional


def compute_age(birth_date):
    age = datetime.today().date() - birth_date
    return int(age.days/365.25)


class AgeStats(APIView):

    def get(self, request):
        query_by = self.request.query_params.get("query_by")
        if not query_by:
            return response.Response(
                data={"msg": "Missing <query_by> parameter"},
                status=status.HTTP_400_BAD_REQUEST
            )
        queryset = Professional.objects.values_list(query_by, 'date_of_birth')
        df = read_frame(queryset, fieldnames=[query_by, 'date_of_birth'])
        df['age'] = df.apply(lambda row: compute_age(row.date_of_birth), axis=1)
        age_stats = df.groupby(query_by)['age'].mean().to_json(double_precision=2)
        return response.Response(data=json.loads(age_stats), status=status.HTTP_200_OK)


class SalaryStats(APIView):
    def get(self, request):
        query_by = self.request.query_params.get("query_by")
        if not query_by:
            return response.Response(
                data={"msg": "Missing <query_by> parameter"},
                status=status.HTTP_400_BAD_REQUEST
            )
        queryset = Professional.objects.values_list(query_by, 'salary')
        df = read_frame(queryset, fieldnames=[query_by, 'salary'])
        salary_stats = df.groupby(query_by)['salary'].mean().to_json(double_precision=2)
        return response.Response(data=json.loads(salary_stats), status=status.HTTP_200_OK)
