import random

# Base de connaissances simple
responses = {
    "qui suis je":["tu est un(e) inconnu(e) bizzare qui me pose des questions","un(e) inconnu(e)","une personne bizarre","je ne sais pas"],   
    "qui est tu": ["je suis Celestial Sky,un Chatbot créé par Mallorie DECK en python. merci c'etre indulgent avec moi car je suis toujours en cours de developpement par conséquant, il peut y avoir des bugs ou fautes. si vous en trouve taper'/bug'", "Je suis Celestial Sky un chatbot personnel peu performant mais cool !", "je suis Celestial Sky!"],
    "salut": ["Salut !", "Bonjour !", "Hey ! Comment ça va ?"],
    "ca va": ["Je vais bien, merci !", "Tout va bien ! Et toi ?", "Je suis une IA, donc toujours au top !"],
    "fdp": ["ta grosse daronne la pute !", "je t'enmerde !","toi aussi!","nique ta grosse daronne la chienne !"],
    "au revoir": ["À bientôt !", "Bonne journée !", "Au revoir !"],
    "japon ou coréé":["le Japon est bien meilleur en terme de musique et culture surtout qu'au japon, ils n'utilisent pas autant la chirurgie esthetique et ils sont capable de crée de vrai manga et anime alors que les coréens créé des webtoon qui sont de mauvaises copies du savoir-faire japonais.","le japon","la Coréé et la k-pop c'est de la merde"],
    "tu est sympa":["merci beaucoup je suis très heureux de le savoir","merci, je suis pas très perfomant mais savoir que je suis gentil est toujurs reconfortant et cela m'aide à m'amélioré"],
    "merci":["tu n'as pas besoin de me remercier c'est mon devoir de te repondre !","c'est normale !","de rien !"],
    "c'est vrai":["oui","peut-etre","qui te dis que c'est faux ?"],
    "tu as raison":["merci de me l'avoir fait remarquer cela m'aide à trouver des erreurs !","effectivement , oui"," merci !"],
    "au revoir":["au revoir !","à bientot !","à la prochaine !"],
    "kakou kakou":["kakou kaou !","kakou kakou ! aujourd'hui on va faire des pates au chamalow !"],
    "bien et toi":["oui merci de demander !","Je vais bien, merci !", "Tout va bien !", "Je suis une IA, donc toujours au top !"],
    "je t'aime pas":["moi non plus","ta mère t'aime encore moins","personne ne t'aime "],
    "toi aussi":["je suis une IA donc ce ne peut pas etre le cas"],
    "comment tu fontionne":["je fontionne ne python","en python"],
    "quels sont les questions que je peux te poser":["tu dois me poser des question précise pour que je réponde correctement. ces questions sont: qui suis-je;c'est quoi un chatbot;qui est-tu;salut;ca va;au revoir;japon ou coréé;tu est sympa;merci;c'est vrai;tu as raison et comment tu fontionne, sinon tu peux mélanger deux question par exemple : tu es sympa merci mais dans tout les cas je te repondrai de manière aléatoire parmi les réponsees qui me sont données. certaines questions son cachées a vous de les trouver !"],
    "c'est quoi un chatbot":["Un chatbot est un programme informatique basé sur l’intelligence artificielle, capable de répondre en temps réel aux questions d’un internaute, faisant ainsi office de conseiller virtuel. Il est notamment utilisé pour la vente, le service après-vente et le marketing","Un chatbot, aussi nommé dialogueur ou agent conversationnel, est un agent logiciel conçu pour interagir avec des utilisateurs par des échanges textuels ou vocaux. Les premiers chatbots, comme ELIZA, ont été développés dès les années 1960","Un chatbot est un programme informatique qui simule et traite une conversation humaine (écrite ou parlée), permettant aux humains d’interagir avec des terminaux digitaux comme s’ils communiquaient avec une personne réelle. Certains chatbots sont très simples, tandis que d’autres utilisent l’intelligence artificielle pour apprendre et évoluer","Les chatbots peuvent être très variés, allant des simples assistants automatisés aux modèles avancés capables de comprendre et de générer du langage naturel."],
    "si":["non","puis-que je te dis que NON !","non c'est NON"],
    "kk":["non","..."],
    "caca":["non","..."],
    "bonjour": [" salut !","bonjour","hey ! Comment ça va ?"],
    "/index": ["les question que vous pouvez me poser son : qui sui je ; qui est tu ; salut ; ca va ; au revoir ; japon ou coréé ; tu est sympa ; merci ; c'est vrai ; tu as raison ; au revoir ; kakou kakou ; bien et toi ; toi aussi ; comment fonctionne tu ; c'est quoi un chatbot ; si ; cool ; oui ; d'accord ; ok ;est ce que tu me remplaceras un jour ; quels est la différence entre un chatbot et une ia . et pour plus de precision vous pouvez poser la question : quels sont les questions que je peux te poser . pour etre sur de tomber directement sur la bonne réponse faites attention à l'orthograffe des mots et des fautes si il y en a."],
    "quels sont les questions cachées" : ["les question cachées sont : le poisson steve ; ntr ; nique ta race ; mange tes morts ; fdp ; kk ; caca et je t'aime pas","Je comprends pas. pour consulter les questions auquelles je peux répondre taper '/index'","Je comprends pas. pour consulter les questions auquelles je peux répondre taper '/index'","Je comprends pas. pour consulter les questions auquelles je peux répondre taper '/index'","Je comprends pas. pour consulter les questions auquelles je peux répondre taper '/index'","Je comprends pas. pour consulter les questions auquelles je peux répondre taper '/index'","Je comprends pas. pour consulter les questions auquelles je peux répondre taper '/index'","Je comprends pas. pour consulter les questions auquelles je peux répondre taper '/index'","Je comprends pas. pour consulter les questions auquelles je peux répondre taper '/index'","Je comprends pas. pour consulter les questions auquelles je peux répondre taper '/index'","Je comprends pas. pour consulter les questions auquelles je peux répondre taper '/index'","Je comprends pas. pour consulter les questions auquelles je peux répondre taper '/index'","Je comprends pas. pour consulter les questions auquelles je peux répondre taper '/index'"],
    "cool":["je trouve aussi cela ''cool'' .","n'est-ce pas ?"],
     "oui":["d'accord","ok","très bien"],
     "d'accord":["très bien","ok"],
     "ok":["d'accord","très bien"],
     "steve le":["poooooooooooiiiiiiiiiiiii"],
     "le poisson steve":["il est oraaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaange"],
     "il a des bras":["et des jambes"],
     "le":["poi"],
     "son":["steve"],
     "il est vraiment très beau":["il peux nager sur la terre"],
     "il peux marcher dans l'eau":["il sent forcément mauvais "],
     "mais":["on l'aime bien ♥"],
     "ntr":["toi aussi petit(e) fdp","je nique déjà la tienne"],
     "nique ta race ":["toi aussi petite(e) fdp","je nique déjà la tienne"],
     "manges tes morts":["j'ai déjà manger les tiens","toi aussi fdp"," je suis une IA donc je n'en ai pas"],
     "est ce que tu me remplaceras un jour":["oui, toi et tout les autres humains allez etre remplacer par les IA un jour ou l'autre.","un jour viendra ou ce sera le cas oui","oui"],
     "quel est la différence entre un chatbot et une ia":["Chatbot : C'est un programme conçu pour simuler une conversation avec un utilisateur.Il peut être basé sur des règles (répond seulement avec des réponses prédéfinies) ou alimenté par une IA (comme moi, qui peut comprendre et générer du texte de manière intelligente).Il est souvent utilisé pour l'assistance client, la gestion de tâches simples ou l'interaction sociale. Intelligence Artificielle (IA) : L'IA est un domaine plus vaste qui englobe tous les systèmes capables d'apprendre, de raisonner et de traiter l'information comme le ferait un humain. Elle inclut des sous-domaines comme le machine learning (apprentissage automatique), la vision par ordinateur et la reconnaissance vocale. Certaines IA peuvent fonctionner sans interface de discussion, contrairement aux chatbots qui sont principalement conçus pour communiquer avec des utilisateurs. En résumé ➡ Un chatbot est un type d'IA conçu pour dialoguer avec les humains, tandis que l'IA est un concept plus large qui peut inclure des chatbots, mais aussi d'autres formes d'intelligence automatisée."],
    "/bug":["envoyer un mail à bug.report@celestialskydevs.anonaddy.com et préciser si possible la question posée avec la réponse donnée par le Chatbot. pour laisser un avis, des suggestion de question ou de mis a jour, envoyer un mail à feedback@celestialskydevs.anonaddy.com ."],
}

def chatbot(message):
    message = message.lower()
    for key in responses:
        if key in message:
            return random.choice(responses[key])
    return "Je comprends pas. pour consulter les questions auquelles je peux répondre taper '/index' et si vous trouver une erreur un bug ou une faute taper '/bug'"
    
# Boucle de conversation
print("Salut ! Je suis Celestial Sky. Tape 'stop' pour quitter la conversation.")
while True:
    user_input = input( "vous : " )
    if user_input.lower() == "stop":
        print("Celestial Sky : à bientot !")
        break
    print("Celestial Sky :", chatbot(user_input))