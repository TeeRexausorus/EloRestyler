templatePole = '''
<div class="card">
  <div class="pole">
      <div class="poleName">{pole}</div>
      <div class="close">x</div>
    </div>
    {line}
</div>
'''
templateLine = '''
  <div class="line">
    <div class="title">{title}</div>
    <div class="subtitle">{subtitle}</div>
    <div class="price">{price}</div>
  </div>
  '''
templateAi = '''
<div class="aiOpinion">
  <div class="criticCard">
    <div class="poleName">L'avis du critique</div>
    <div class="close">x</div>
  </div>
    <div class="critic">
        {text}
    </div>
</div>'''
templateClock = '''
<div class="footer">
  <span class="clock">{day}</span>
  <div class="message"><span>\"{message}\"</span><span>Pensez à recharger votre solde sur https://popandpay2.com, site INITIALE</span></div>
</div>
'''
headerHtml = '''
<head>
  <link href="https://fonts.cdnfonts.com/css/w95fa" rel="stylesheet">
  <link href="https://fonts.cdnfonts.com/css/roboto-serif" rel="stylesheet">
  <link href="testElo.css" rel="stylesheet" />
</head>
<body>
<div class="cards">
'''
messages = [
    "C’est d’la merde, c’est tout. Moi on me sert ça dans une auberge, le tavernier il s’prend une quiche dans sa tête.",
    "Je ne mange pas de graine !",
    "Serpent ! Je ne mange pas de ce pain là !",
    "Les fraises, en fait, quand on leur fout la paix, elles sont consommables !",
    "On dira ce qu'on veut, la France ça reste le pays des 400 fromages.",
    "Y'a des gens qui ont pris la peine de faire un dessert, la moindre des choses, c'est de rester pour le manger.",
    "Faut pas respirer la compote, ça fait tousser.",
    "Comment est votre blanquette ?",
    "Sans vouloir la ramener, la seule différence concrète avec des briques, c'est que vous appelez ça des tartes !",
    "On peut discuter, mais je préviens, ça va vite me gonfler.",
    "Faut pas s’amuser à attaquer ça avec des dents de lait, hein.",
    "On me dit le plus grand bien des harengs pommes à l'huile ?",
    "Joyeux Hunger Games, et puisse le sort vous être favorable !",
    "Tout à l'heure, on a vu que le chapelet de saucisses de toulouse n'était pas un objet redondant. Et pourtant, on a pu lui trouver une utilisation périmétrique en s'en servant comme un fouet.",
    "J'aime me beurrer la biscotte.",

]

promptBasicMessage = "Tu es un critique culinaire de renom qui utilise des figures de style variées dans ses avis, sans mettre en avant les figures de style utilisées, tu peux utiliser des retours à la ligne. Qu'as-tu à dire sur le menu de cantine de restaurant inter-entreprise suivant :"
prompt = "Plat : {plat} {subtitle}"
