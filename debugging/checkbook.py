# Définition de la classe Checkbook
class Checkbook:
    # Fonction spéciale qui s'appelle quand on crée un objet Checkbook
    def __init__(self):
        self.balance = 0.0  # Le solde du compte commence à 0.0

    # Méthode pour déposer de l'argent
    def deposit(self, amount):
        self.balance += amount  # Ajoute le montant au solde
        print("Deposited ${:.2f}".format(amount))  # Affiche combien on a déposé
        print("Current Balance: ${:.2f}".format(self.balance))  # Affiche le solde actuel

    # Méthode pour retirer de l'argent
    def withdraw(self, amount):
        if amount > self.balance:  # Vérifie si on a assez d'argent
            print("Insufficient funds to complete the withdrawal.")  # Message si pas assez
        else:
            self.balance -= amount  # Soustrait le montant du solde
            print("Withdrew ${:.2f}".format(amount))  # Affiche combien on a retiré
            print("Current Balance: ${:.2f}".format(self.balance))  # Affiche le solde actuel

    # Méthode pour afficher le solde sans rien changer
    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))  # Affiche juste le solde

# Fonction principale du programme
def main():
    cb = Checkbook()  # Crée un nouveau compte Checkbook
    while True:  # Boucle infinie pour que l'utilisateur continue à utiliser le compte
        # Demande à l'utilisateur ce qu'il veut faire
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()  
        # .lower() transforme la réponse en minuscules pour accepter toutes les écritures

        if action == 'exit':  # Si l'utilisateur tape 'exit', on quitte le programme
            break

        elif action == 'deposit':  # Si l'utilisateur veut déposer de l'argent
            try:
                # Demande combien déposer et convertit en nombre
                amount = float(input("Enter the amount to deposit: $"))  
                if amount <= 0:  # Vérifie que le montant est positif
                    print("Amount must be positive!")  # Message d'erreur si négatif ou zéro
                else:
                    cb.deposit(amount)  # Appelle la méthode deposit pour ajouter l'argent
            except ValueError:  # Si l'utilisateur ne tape pas un nombre
                print("Invalid input. Please enter a number.")  # Message d'erreur

        elif action == 'withdraw':  # Si l'utilisateur veut retirer de l'argent
            try:
                # Demande combien retirer et convertit en nombre
                amount = float(input("Enter the amount to withdraw: $"))  
                if amount <= 0:  # Vérifie que le montant est positif
                    print("Amount must be positive!")  # Message d'erreur si négatif ou zéro
                else:
                    cb.withdraw(amount)  # Appelle la méthode withdraw pour retirer l'argent
            except ValueError:  # Si l'utilisateur ne tape pas un nombre
                print("Invalid input. Please enter a number.")  # Message d'erreur

        elif action == 'balance':  # Si l'utilisateur veut voir le solde
            cb.get_balance()  # Appelle la méthode get_balance pour afficher le solde

        else:  # Si l'utilisateur tape n'importe quoi d'autre
            print("Invalid command. Please try again.")  # Message d'erreur

# Ce code se lance seulement si le fichier est exécuté directement (pas importé)
if __name__ == "__main__":
    main()  # Appelle la fonction principale pour démarrer le programme
