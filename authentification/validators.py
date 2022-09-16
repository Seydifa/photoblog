from django.core.exceptions import ValidationError


class ContainsLetterValidator:

    def validate(self, password, user=None):
        if not any(char.isalpha() for char in password):
            raise ValidationError(
                "Le mot de passed doit contenir une lettre", code='password_no_letter'
            )

    def get_help_text(self):
        return "Le mot de passe doit contenir au moins une lettre majuscule et minuscule"
