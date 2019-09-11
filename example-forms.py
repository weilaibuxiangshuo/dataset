from django import forms
from utils.forms import FormMixin
from .models import Data, DealType
import re


class DataFrom(forms.Form, FormMixin):
	title = forms.CharField(max_length=64, required=True,
							error_messages={"required": "数据类型名不能为空", "max_length": "数据类型名过长"})


class DealTypeFrom(forms.Form, FormMixin):
	title = forms.CharField(max_length=32, required=True,
							error_messages={"required": "交易类型名不能为空", "max_length": "交易类型名过长"})


class DataCardFrom(forms.Form, FormMixin):
	card_number = forms.CharField(max_length=32, required=True,
								  error_messages={"required": "数据卡号不能为空", "max_length": "数据卡名称过长"})
	name = forms.CharField(max_length=32, required=True,
						   error_messages={"required": "开户人不能为空", "max_length": "开户人名称过长"})
	dealTypeId = forms.IntegerField(required=True, error_messages={"required": "数据卡类型不能为空"})
	DataId = forms.IntegerField(required=True, error_messages={"required": "数据不能为空"})
	balance = forms.CharField(required=True, error_messages={"required": "余额不能为空"})

	def clean(self):
		cleaned_data = super(DataCardFrom, self).clean()

		balance = cleaned_data.get("balance")
		if not re.match("^(-?\d+)(\.\d+)?$", balance):
			raise forms.ValidationError("余额必须是数字")

		DataId = cleaned_data.get("DataId")
		DataList = Data.objects.filter(id=DataId)
		if not DataList:
			raise forms.ValidationError("所选数据不存在")

		dealTypeId = cleaned_data.get("dealTypeId")
		dealTypeList = DealType.objects.filter(id=dealTypeId)
		if not dealTypeList:
			raise forms.ValidationError("所选数据卡类型不存在")

		card_number = cleaned_data.get("card_number")
		if not card_number.isdigit():
			raise forms.ValidationError("数据卡号必须是数字")
