Django Form -- 字段的用法扩展
form.py的代码
from django import forms
from django.forms import fields
from django.forms import widgets
 
class DetailForm(forms.Form):
 
    inp = fields.CharField()
    
required
inp = fields.CharField(required=False)　　#表单可以为空　
inp = fields.CharField(required=True)　　 #表单不可以为空

label
inp = fields.CharField(label='inp_no1')　
应用：点击label标签，光标聚焦在输入框中 (以下两种方法都能实现)
<form action="/detail/" method="POST">
    {% csrf_token %}
    <p>
        {{ obj.inp.label_tag }}
        {{ obj.inp }}
        <span>{{ obj.errors.inp.0 }}</span>
    </p>
    <p>
        <input type="submit" value="提交">
    </p>
</form>

<form action="/detail/" method="POST">
    {% csrf_token %}
    <p>
        <label for={{  obj.inp.id_for_label }}>{{ obj.inp.label }}</label>
        {{ obj.inp }}
        <span>{{ obj.errors.inp.0 }}</span>
    </p>
    <p>
        <input type="submit" value="提交">
    </p>
</form>

initial 
inp = fields.CharField(initial='python')　　#设置填充表单的默认值
error_messages
inp = fields.CharField(error_messages={'required': '不能为空', 'invalid': '格式错误'})　 #自定义错误信息
show_hidden_initial
inp = fields.CharField(show_hidden_initial=True)　　#前端页面自动生成一个隐藏的input标签，表单提交后，会将表单值赋值给隐藏标签，可用于检验两次输入是否一致
label_suffix
inp = fields.CharField(label_suffix='-')　　#自定义Label内容后缀为 "-"　


Django Form -- 对单个表单的组合验证

fields.ComboField()  -- 将多个fields的验证功能组合到一个表单上
from django import forms
from django.forms import fields
 
class DetailForm(forms.Form):
 
    inp = fields.ComboField(fields= [fields.CharField(max_length=20), fields.EmailField(), ])
    
    
