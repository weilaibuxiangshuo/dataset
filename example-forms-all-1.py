Django Form -- 自定义字段的规则验证和错误提示
error_messages=None
validators=[]

from django import forms
from django.forms import fields
from django.forms import widgets
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

自定义验证规则方式一：
 class DetailForm(forms.Form):
     inp = fields.Field(
         #表单输入必须是数字，并且数字必须是159开头
        validators=[RegexValidator(r'^[0-9]+$', '请输入数字'), RegexValidator(r'^159[0-9]+$', '数字必须以159开头')],
        )
      
自定义验证规则方式二：
#定义验证规则的函数
def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')
 
class DetailForm(forms.Form):
    # 使用自定义验证规则
    inp = fields.Field(validators=[mobile_validate, ],
                            error_messages={'required': '手机不能为空'},
                            widget=widgets.TextInput(attrs={'placeholder': u'手机号码'}))
                            
                            
自定义验证规则方式三：
class DetailForm(forms.Form):
    inp = fields.Field(
        validators=[RegexValidator(r'^[0-9]+$', '格式错误', 'invalid')],
    )
     #二次验证函数的名字是固定写法，以clear_开头，后面跟上字段的变量名
    def clean_inp(self):
         #通过了validators的验证之后，在进行二次验证
        value = self.cleaned_data['inp']
        if "123" in value:
            raise ValidationError('内容不符合要求', 'invalid')
 
        #通过了二次验证之后，返回表单数据，通过value_dic = obj.clean()能够得到验证通过后的表单数据
        return value
 
 自定义错误
class DetailForm(forms.Form):
    inp = fields.Field(
         #error_messages中的err1与RegexValidator中的code='err1'对应
        #error_messages的优先级高，如果表单输入的不是数字，会提示 '类型不符合要求'
        validators=[RegexValidator(r'^[0-9]+$', '请输入数字', code='err1'), RegexValidator(r'^159[0-9]+$', '数字必须以159开头', code='err2')],
        error_messages={'err1': '类型不符合要求', 'err2': '格式不符合要求'}
        )
        
        
  
