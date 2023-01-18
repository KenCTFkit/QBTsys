from django import forms
#モデルクラスを呼出
from .models import QBTModel
#フォームクラス作成
class QBTForm(forms.Form):
    
    TemperatureA = forms.ChoiceField(
        label='体温',
        choices = (
            (32, 32),
            (33, 33),
            (34, 34),
            (35, 35),
            (36, 36),
            (37, 37),
            (38, 38),
            (39, 39),
            (40, 40),
            (41, 41),
            (42, 42),
        ),
        initial=36,
        required=True,
        widget=forms.widgets.Select(),
    )

    TemperatureB = forms.ChoiceField(
        choices = (
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
        ),
        initial=0,
        required=True,
        widget=forms.widgets.Select(),
    )

    Q1 = forms.BooleanField(
        label='風邪症状はありますか？',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'check'}),
    )

    Q2 = forms.BooleanField(
        label='倦怠感はありますか？',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'check'}),
    )


    FreeText = forms.CharField(
        label = 'その他の症状',
        required=False, #必須項目か？
        max_length=100,
        widget=forms.Textarea,
    )    
    
    def save(self, username):
        # save data using the self.cleaned_data dictionary
        data = self.cleaned_data
        post = QBTModel(StudentID=username, TemperatureA=data['TemperatureA'], TemperatureB=data['TemperatureB'], Q1=data['Q1'], Q2=data['Q2'], FreeText=data['FreeText'])
        post.save()
 
