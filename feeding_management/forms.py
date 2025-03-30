from django import forms
from .models import FeedingChart


class FeedingChartForm(forms.ModelForm):
    class Meta:
        model = FeedingChart
        fields = [
            'breakfast_feed', 'breakfast_quantity',
            'lunch_feed', 'lunch_quantity',
            'dinner_feed', 'dinner_quantity',
            'hay', 'hay_quantity',
            'supplements', 'medicines', 'notes'
        ]
        widgets = {
            'breakfast_feed': forms.TextInput(attrs={'class': 'form-control'}),
            'lunch_feed': forms.TextInput(attrs={'class': 'form-control'}),
            'dinner_feed': forms.TextInput(attrs={'class': 'form-control'}),
            'hay': forms.TextInput(attrs={'class': 'form-control'}),
            'supplements': forms.TextInput(attrs={'class': 'form-control'}),
            'medicines': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}),
        }

    def clean(self):
        cleaned_data = super().clean()

        meal_fields = [
            ('breakfast_feed', 'breakfast_quantity'),
            ('lunch_feed', 'lunch_quantity'),
            ('dinner_feed', 'dinner_quantity'),
            ('hay', 'hay_quantity')
        ]

        for feed_field, qty_field in meal_fields:
            feed = cleaned_data.get(feed_field)
            qty = cleaned_data.get(qty_field)

            if feed and qty is None:
                self.add_error(
                    qty_field, 
                    f"Please specify quantity for {feed_field.replace(
                        '_', ' ')}.")
            if qty and not feed:
                self.add_error(
                    feed_field, 
                    f"Please specify feed type for {qty_field.replace(
                        '_', ' ')}.")

            if qty is not None and qty <= 0:
                self.add_error(
                    qty_field, "Quantity must be a positive number.")

        return cleaned_data
