#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <unistd.h> //pour utiliser la fonction usleep() sur Unix/Linux

int main(int argc, char *argv[]) {
    //Présentation
    for (int i = 0; "Bonjour et bienvenue !\n\n"[i] != '\0'; i++) {
        printf("%c", "Bonjour et bienvenue !\n\n"[i]);
        fflush(stdout);
        usleep(3000);
    }

     char reponse[4];

    // Demander le nom du joueur
    for (int i = 0; "Comment souhaites-tu t'appeler ?\n"[i] != '\0'; i++) {
        printf("%c", "Comment souhaites-tu t'appeler ?\n"[i]);
        fflush(stdout);
        usleep(3000);
    }
    char nom[20];
    scanf("%s", nom);

    // Confirmer le nom du joueur
    do {
        char message[50];
        sprintf(message, "\n Tu souhaites bien t'appeler %s ?\n Oui ou Non ? \n ", nom);
        for (int i = 0; message[i] != '\0'; i++) {
            printf("%c", message[i]);
            fflush(stdout);
            usleep(3000);
        }
        scanf("%s", reponse);

        // Convertir la réponse en minuscules
        for (int i = 0; reponse[i]; i++) {
            reponse[i] = tolower(reponse[i]);
        }

        if (strcmp(reponse, "oui") == 0) {
            printf("Parfait %s, passons a la suite !\n", nom);
            break;
        } else if (strcmp(reponse, "non") == 0) {
            printf(".\n");
        } else {
            printf("Je n'ai pas compris ta reponse. Reponds par 'Oui' ou 'Non' !\n");
        }

    } while (strcmp(reponse, "oui") != 0 && strcmp(reponse, "non") != 0);



      // Initialiser les statistiques du joueur
    int nombreDeVies = 3;
    int niveau = 1;
    int force = 5;
    int intelligence = 5;
    int constitution = 5;
    int pointCompetence = 0;

    // Afficher les statistiques du joueur
    char message[100];
    sprintf(message, "\n Tu as a present %d vies et tu es niveau %d \n Tes statistiques sont :\n%d en force\n%d en intelligence\n%d en constitution.\n\n", nombreDeVies, niveau, force, intelligence, constitution);
    for (int i = 0; message[i] != '\0'; i++) {
        printf("%c", message[i]);
        fflush(stdout);
        usleep(3000);
    }

    // Commencer le jeu
    for (int i = 0; "On commence ?\nC'est parti !\n...\n...\n"[i] != '\0'; i++) {
        printf("%c", "On commence ?\nC'est parti !\n...\n...\n"[i]);
        fflush(stdout);
        usleep(2000);
    }

    // Modifier le nombre de vies du joueur

    for (int i = 0; "BAM\n"[i] != '\0'; i++) {
    printf("%c", "BAM\n"[i]);
    fflush(stdout);
    usleep(2000);
}

for (int i = 0; "Oh non, tu as percute un ennemi !\n"[i] != '\0'; i++) {
    printf("%c", "Oh non, tu as percute un ennemi !\n"[i]);
    fflush(stdout);
    usleep(2000);
}
nombreDeVies = 2;

char messageVie[200];
sprintf(messageVie, "\n Il ne te reste plus que %d vies desormais !\n\n",nombreDeVies);
for (int i = 0; messageVie[i] != '\0'; i++) {
    printf("%c", messageVie[i]);
    fflush(stdout);
    usleep(3000);
}

    return 0;
}
