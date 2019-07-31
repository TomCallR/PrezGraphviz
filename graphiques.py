#%% Schéma de la bibliothèque
from graphviz import Digraph

#
schema = Digraph(
    name='Schema_Graphviz',
    # comment='Schéma du fonctionnement',
    filename='graphs/schema_graphviz',
    format='svg',
    # other possible formats : png, gv, jpeg, ps, svg ....
    # cf https://www.graphviz.org/doc/info/output.html
    engine='dot'
)
schema.attr(label='Fonctionnement de la bibliothèque graphviz')
schema.attr(labelloc='t')
schema.attr('node', shape='box')
schema.node('graph_object', 'génération de l\'objet Graph en Python')
schema.node('dot_file', 'génération du fichier DOT')
schema.node('display', 'affichage')
schema.edge('graph_object', 'dot_file')

sub = Digraph(
    name='cluster_graphviz',
    engine='dot'
)
sub.attr(label=' Logiciel Graphviz')
sub.attr('node', shape='ellipse')
sub.node('graphviz', 'exécution de Graphviz')
sub.node('viz_file', 'génération du fichier "image"')
sub.edge('graphviz', 'viz_file')
schema.subgraph(sub)

schema.edge('dot_file', 'graphviz')
schema.edge('viz_file', 'display')
schema.render()


#%% Partie Vocabulaire : exemple généalogie
import graphviz
gno = graphviz.Graph('Arbre_no',
    filename='graphs/genealogie_no',
    format='jpg',
    engine='dot')
gno.attr(label='Graphe non orienté')
gno.attr(labelloc='t')
gno.node('M', 'Marie Slodowska')    
gno.node('P', 'Pierre Curie')
gno.node('I', 'Irène Curie')
gno.edge('M', 'I')
gno.edge('P', 'I')
gno.render()

go = graphviz.Digraph('Arbre_o', 
    filename='graphs/genealogie_o',
    format='jpg',
    engine='dot')
go.attr(label='Graphe orienté')
go.attr(labelloc='t')
go.node('M', 'Marie Slodowska')
go.node('P', 'Pierre Curie')
go.node('I', 'Irène Curie')
go.edge('M', 'I')
go.edge('P', 'I')
go.render()


#%% Exemple osage
import graphviz
os = graphviz.Graph(
    name='osage',
    filename='graphs/osage',
    format='jpg',
    engine='osage'
)
with os.subgraph(
    name='cluster1'
) as c1:
    c1.node('A', label='A')
    c1.node('B', label='B')
with os.subgraph(
    name='cluster2'
) as c2:
    c2.node('C', label='C')
    with c2.subgraph(
        name='cluster3'
    ) as c3:
        c3.node('D', label='D')
        c3.node('E', label='E')
os.render()


#%% Exemple de patchwork
import graphviz
pw = graphviz.Graph(
    name='patchwork',
    filename='graphs/patchwork',
    format='jpg',
    engine='patchwork'
)
with pw.subgraph(
    name='cluster1'
) as c1:
    c1.node('A', label='A1', area='1')
    c1.node('B', label='B2', area='2') 
with pw.subgraph(
    name='cluster2'
) as c2:
    c2.node('C', label='C3', area='3')
    with c2.subgraph(
        name='cluster3'
    ) as c3:
        c3.node('D', label='D2', area='2')
        c3.node('E', label='E5', area='5')
pw.render()


#%% Exercice V2 avec noeuds HTML
import graphviz
bdd = graphviz.Digraph(
    name='bdd',
    filename='graphs/bdd',
    format='jpg',
    engine='dot',
    node_attr={'shape': 'none'},
    graph_attr={'rankdir': 'LR',
                'label': 'BDD hôpital',
                'labelloc': 't'}
)

bdd.node('pat', '''<
    <table border="0" cellborder="1" cellspacing="0">
        <tr><td bgcolor="yellow">pat</td></tr>
        <tr><td port="pat_id">id</td></tr>
        <tr><td>nom</td></tr>
        <tr><td>prenom</td></tr>
        <tr><td>date_naissance</td></tr>
        <tr><td>sexe</td></tr>
        <tr><td>statut_vital</td></tr>
        <tr><td>date_deces</td></tr>
    </table>>''')

bdd.node('sej', '''<
    <table border="0" cellborder="1" cellspacing="0">
        <tr><td bgcolor="yellow">sej</td></tr>
        <tr><td port="sej_id">id</td></tr>
        <tr><td port="sej_patient_id">patient_id</td></tr>
        <tr><td>date_entree</td></tr>
        <tr><td>date_sortie</td></tr>
        <tr><td>mode_sortie</td></tr>
    </table>>''')

bdd.node('mvt', '''<
    <table border="0" cellborder="1" cellspacing="0">
        <tr><td bgcolor="yellow">mvt</td></tr>
        <tr><td port="mvt_id">id</td></tr>
        <tr><td port="mvt_sejour_id">sejour_id</td></tr>
        <tr><td port="mvt_service_id">service_id</td></tr>
        <tr><td>date_entree</td></tr>
        <tr><td>date_sortie</td></tr>
    </table>>''')

bdd.node('srv', '''<
    <table border="0" cellborder="1" cellspacing="0">
        <tr><td bgcolor="yellow">srv</td></tr>
        <tr><td port="srv_id">id</td></tr>
        <tr><td port="srv_parent_id">parent_id</td></tr>
        <tr><td>nom</td></tr>
        <tr><td>categorie</td></tr>    
    </table>>''')

bdd.edge('sej:sej_patient_id', 'pat:pat_id',
        headlabel='1', taillabel='0,n')
bdd.edge('mvt:mvt_sejour_id', 'sej:sej_id',
        headlabel='1', taillabel='0,n')
bdd.edge('srv:srv_parent_id', 'srv:srv_id',
        headlabel='1', taillabel='0,n')
bdd.edge('mvt:mvt_service_id', 'srv:srv_id',
        headlabel='1', taillabel='0,n')
bdd.view()


#%% Aide exercice : exemple de noeud HTML
import graphviz
bdd_help = graphviz.Graph(
    name='bdd_help',
    filename='graphs/bdd_help',
    format='jpg'
)
bdd_help.node('matable', '''<
    <table>
    <tr><td bgcolor="yellow">matable</td></tr>
    <tr><td>id</td></tr>
    </table>>''')
bdd_help.view()

#%%
