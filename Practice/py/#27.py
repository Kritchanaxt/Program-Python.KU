
#? Test #3

class EmailValidator:
    def __init__(self, email):
        self.email = email

    def is_valid(self):
        if '@' not in self.email:
            return False
        
        local_part, domain = self.email.split('@', 1)
        return self.is_valid_local_part(local_part) and self.is_valid_domain(domain)
    
    def is_valid_local_part(self, local_part):
        valid_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-"

        if not local_part or local_part[0] in '._-' or local_part[-1] in '._-':
            return False
        
        return all(char in valid_chars for char in local_part)
    
    def is_valid_domain(self, domain):
        if '.' not in domain or domain.startswith('.') or domain.endswith('.'):
            return False
        
        parts = domain.split('.')
        return all(self.is_valid_domain_part(part) for part in parts) and len(parts[-1]) >= 2

    def is_valid_domain_part(self, part):
        return part.isalnum()
    
emails = ["abc-@mail.com", "abc.def@,ail.com", "abc.def@mail-archive.com", "abc.def@mail.org", "abc@com", "abc#def@mail.com"]

for email in emails:
    validator = EmailValidator(email)
    print(f"{email}: {'Valid' if validator.is_valid() else 'Invalid'}")