from django import forms

class AddGame(forms.Form):
    game_name = forms.CharField(label="Game name", max_length=200)
    game_type = forms.CharField(label="Game type", max_length=100)