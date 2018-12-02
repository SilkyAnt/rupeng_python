from django import forms


class addForms(forms.Form):
    a = forms.IntegerField(label="数字A", error_messages={"required": "请输入一个整数"})
    b = forms.IntegerField(label="数字A", error_messages={"required": "请输入一个整数"})


class RegisterForm(forms.Form):
    name = forms.CharField(label="请输入用户名：", min_length="4", max_length="8",
                           error_messages={"required": "名字不能为空！",
                                           "min_length": "长度不能少于4",
                                           "max_length": "长度不能大于8"})

    password = forms.CharField(label="请输入密码", min_length="6", max_length="10",
                               widget=forms.PasswordInput(attrs={"placeholder": "请输入密码"}))
    telephont = forms.IntegerField(label="请输入电话号码:")
    email = forms.EmailField(label="请输入电子信箱:")
    is_married = forms.BooleanField(label="是否结婚:")
    # 如果要限制出生年的选择
    # BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
    # birth_date = forms.DateField(label="出生日期", widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    birth_date = forms.DateField(label="出生日期", widget=forms.SelectDateWidget())

    FAVORITE_COLORS_CHOICES = {
        ("blue", "BLUE"),
        ("green", "GREEN"),
        ("black", "BLACK")
    }
    favorite_colors = forms.MultipleChoiceField(
        label="请选择你喜欢的颜色：",
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES
    )
