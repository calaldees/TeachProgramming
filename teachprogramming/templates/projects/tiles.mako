<%inherit file="_project.mako"/>

<%
    vername = {
        'base'          :'1',
        'player'        :'1,player',
        'blocks'        :'1,player,blocks',
        'blocks_random' :'1,player,blocks,blocks_random',
        'limit'         :'1,player,blocks,limit',
        'eat'           :'1,player,blocks,blocks_random,limit,eat',
        'images'        :'1,player,blocks,images',
        'full'          :'1,player,blocks,blocks_random,limit,eat,images',
    }
%>



<h1>Tiles</h1>

${parent.web_demo(vername['full'])}


<h2>Base</h2>
${self.show_diff(None,vername['base'])}

<h2>Player</h2>
${self.show_diff(vername['base'],vername['player'])}

<h2>Blocks</h2>
${self.show_diff(vername['player'],vername['blocks'])}
<h3>Blocks Random</h3>
${self.show_diff(vername['blocks'],vername['blocks_random'])}

<h2>eat</h2>
${self.show_diff(vername['blocks_random'],vername['eat'])}

<h2>limit</h2>
${self.show_diff(vername['blocks'],vername['limit'])}

<h2>images</h2>
${self.show_diff(vername['blocks'],vername['images'])}