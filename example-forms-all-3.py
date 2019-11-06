Django Form -- ChoiceField字段

ChoiceField
from django import forms
from django.forms import fields
 
class DetailForm(forms.Form):
 
    inp = fields.ChoiceField(
        initial=2,
        choices=((1, 'SH'), (2, 'BJ'))
    )
    
ChoiceField字段只能返回字符，value_dic = obj.clean()的结果是{'inp': '2'}

TypedChoiceField  -- 带有类型转换功能的下拉框
from django import forms
from django.forms import fields
 
class DetailForm(forms.Form):
 
    inp = fields.MultipleChoiceField(
        initial=[1, 2],
        choices=((1, 'SH'), (2, 'BJ'))
    )
value_dic = obj.clean()的结果是{'inp': ['1', '2']}

TypedMultipleChoiceField
from django import forms
from django.forms import fields
 
class DetailForm(forms.Form):
 
    inp = fields.TypedMultipleChoiceField(
        coerce=lambda x: int(x),
        initial=[1, 2],
        choices=((1, 'SH'), (2, 'BJ'))
    )
    
value_dic = obj.clean()的结果是{'inp': [1, 2]}
