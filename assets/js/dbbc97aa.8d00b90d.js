"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[377],{3905:(e,a,o)=>{o.d(a,{Zo:()=>d,kt:()=>v});var t=o(7294);function n(e,a,o){return a in e?Object.defineProperty(e,a,{value:o,enumerable:!0,configurable:!0,writable:!0}):e[a]=o,e}function r(e,a){var o=Object.keys(e);if(Object.getOwnPropertySymbols){var t=Object.getOwnPropertySymbols(e);a&&(t=t.filter((function(a){return Object.getOwnPropertyDescriptor(e,a).enumerable}))),o.push.apply(o,t)}return o}function i(e){for(var a=1;a<arguments.length;a++){var o=null!=arguments[a]?arguments[a]:{};a%2?r(Object(o),!0).forEach((function(a){n(e,a,o[a])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(o)):r(Object(o)).forEach((function(a){Object.defineProperty(e,a,Object.getOwnPropertyDescriptor(o,a))}))}return e}function s(e,a){if(null==e)return{};var o,t,n=function(e,a){if(null==e)return{};var o,t,n={},r=Object.keys(e);for(t=0;t<r.length;t++)o=r[t],a.indexOf(o)>=0||(n[o]=e[o]);return n}(e,a);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);for(t=0;t<r.length;t++)o=r[t],a.indexOf(o)>=0||Object.prototype.propertyIsEnumerable.call(e,o)&&(n[o]=e[o])}return n}var p=t.createContext({}),l=function(e){var a=t.useContext(p),o=a;return e&&(o="function"==typeof e?e(a):i(i({},a),e)),o},d=function(e){var a=l(e.components);return t.createElement(p.Provider,{value:a},e.children)},m="mdxType",u={inlineCode:"code",wrapper:function(e){var a=e.children;return t.createElement(t.Fragment,{},a)}},c=t.forwardRef((function(e,a){var o=e.components,n=e.mdxType,r=e.originalType,p=e.parentName,d=s(e,["components","mdxType","originalType","parentName"]),m=l(o),c=n,v=m["".concat(p,".").concat(c)]||m[c]||u[c]||r;return o?t.createElement(v,i(i({ref:a},d),{},{components:o})):t.createElement(v,i({ref:a},d))}));function v(e,a){var o=arguments,n=a&&a.mdxType;if("string"==typeof e||n){var r=o.length,i=new Array(r);i[0]=c;var s={};for(var p in a)hasOwnProperty.call(a,p)&&(s[p]=a[p]);s.originalType=e,s[m]="string"==typeof e?e:n,i[1]=s;for(var l=2;l<r;l++)i[l]=o[l];return t.createElement.apply(null,i)}return t.createElement.apply(null,o)}c.displayName="MDXCreateElement"},5174:(e,a,o)=>{o.r(a),o.d(a,{assets:()=>p,contentTitle:()=>i,default:()=>u,frontMatter:()=>r,metadata:()=>s,toc:()=>l});var t=o(7462),n=(o(7294),o(3905));const r={sidebar_position:3,custom_edit_url:null},i="M\xf3dulo agente-reativo-v1",s={unversionedId:"relat\xf3rio/modulo-agente-reativo-v1",id:"relat\xf3rio/modulo-agente-reativo-v1",title:"M\xf3dulo agente-reativo-v1",description:"Descri\xe7\xe3o do Agente Reativo (V1)",source:"@site/docs/relat\xf3rio/modulo-agente-reativo-v1.md",sourceDirName:"relat\xf3rio",slug:"/relat\xf3rio/modulo-agente-reativo-v1",permalink:"/IA_mundo_do_wumpus/docs/relat\xf3rio/modulo-agente-reativo-v1",draft:!1,editUrl:null,tags:[],version:"current",sidebarPosition:3,frontMatter:{sidebar_position:3,custom_edit_url:null},sidebar:"tutorialSidebar",previous:{title:"Ambiente do Mundo do Wumpus",permalink:"/IA_mundo_do_wumpus/docs/relat\xf3rio/modulo-ambiente"},next:{title:"M\xf3dulo agente-reativo-v2",permalink:"/IA_mundo_do_wumpus/docs/relat\xf3rio/modulo-agente-reativo-v2"}},p={},l=[{value:"Descri\xe7\xe3o do Agente Reativo (V1)",id:"descri\xe7\xe3o-do-agente-reativo-v1",level:2},{value:"Expeficica\xe7\xf5es do Agente Reativo (V1)",id:"expeficica\xe7\xf5es-do-agente-reativo-v1",level:2},{value:"Exemplo",id:"exemplo",level:3},{value:"Exemplos <code>2</code>",id:"exemplos-2",level:2},{value:"Tamanho do mundo <code>5x5</code>",id:"tamanho-do-mundo-5x5",level:3}],d={toc:l},m="wrapper";function u(e){let{components:a,...o}=e;return(0,n.kt)(m,(0,t.Z)({},d,o,{components:a,mdxType:"MDXLayout"}),(0,n.kt)("h1",{id:"m\xf3dulo-agente-reativo-v1"},"M\xf3dulo agente-reativo-v1"),(0,n.kt)("h2",{id:"descri\xe7\xe3o-do-agente-reativo-v1"},"Descri\xe7\xe3o do Agente Reativo (V1)"),(0,n.kt)("p",null,"O ",(0,n.kt)("strong",{parentName:"p"},"Agente Reatico V1")," tem como principal caracter\xedstica n\xe3o possuir mem\xf3ria, dessa forma, suas a\xe7\xf5es s\xe3o baseadas no estado atual, para o implementa\xe7\xe3o desse agente foi usada uma classe que interage com a classe do ambiente, assim \xe9 possivel a partir das percep\xe7\xf5es da possi\xe7\xe3o atual obter o pr\xf3ximo passo, para realizar essa a\xe7\xe3o como o agente reativo v1 n\xe3o possui mem\xf3ria, pegamos as possiveis poso\xe7\xf5es que o agente pode se mover e sorteamos aleatoriamente uma delas."),(0,n.kt)("h2",{id:"expeficica\xe7\xf5es-do-agente-reativo-v1"},"Expeficica\xe7\xf5es do Agente Reativo (V1)"),(0,n.kt)("ul",null,(0,n.kt)("li",{parentName:"ul"},"O comportamento do Agente \xe9 definido a partir de seu conjunto de regras:",(0,n.kt)("ul",{parentName:"li"},(0,n.kt)("li",{parentName:"ul"},"Se < percep\xe7\xf5es > ent\xe3o < a\xe7\xe3o >."))),(0,n.kt)("li",{parentName:"ul"},"Este conjunto de regras (ou Base de Conhecimento) deve ser especificado por meio de uma tabela, aos moldes da que foi especificada, inicialmente, na \u201cAula 04';"),(0,n.kt)("li",{parentName:"ul"},"A partir da especifica\xe7\xe3o, o pr\xf3ximo passo \xe9 codificar o Agente e integrar ao \u201cGerador Aleat\xf3rio de Ambientes, de forma a ossibilitar a realiza\xe7\xe3o de testes de valida\xe7\xe3o para posterior avalia\xe7\xe3o de performance;"),(0,n.kt)("li",{parentName:"ul"},"Obs.: Ser\xe3o projetadas v\xe1rias vers\xf5es deste Agente. Nesta primeira vers\xe3o, ele utiliza apenas o conjunto de regras como base de conhecimento. Ou seja, n\xe3o tem mem\xf3ria e nenhum outro mecanismo mais sofisticado para escolher qual das poss\xedveis regras utilizar. Para isto, deve ser uma escolha aleat\xf3ria. Al\xe9m disso, ele tem apenas uma \xfanica flecha.")),(0,n.kt)("h3",{id:"exemplo"},"Exemplo"),(0,n.kt)("h2",{id:"exemplos-2"},"Exemplos ",(0,n.kt)("inlineCode",{parentName:"h2"},"2")),(0,n.kt)("p",null,"Para fazer o jogo execultar at\xe9 obter uma vit\xf3ria, podemos usar loops while aninhados, dessa forma o primeiro loop s\xf3 terminal quando o ouver uma vit\xf3ia, e o segundo loop \xe9 respons\xe1vel por realizar a din\xe1mica do ambiente."),(0,n.kt)("h3",{id:"tamanho-do-mundo-5x5"},"Tamanho do mundo ",(0,n.kt)("inlineCode",{parentName:"h3"},"5x5")),(0,n.kt)("p",null,(0,n.kt)("strong",{parentName:"p"},"C\xf3digo:")),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-python",metastring:'title="main.py"',title:'"main.py"'},'from ia_wumpus import Ambiente\nfrom ia_wumpus import AgenteReativoV1\nimport os\n\nrodadas = 0\npassos = 0\n\nwhile True:\n    passos = 0\n    amb = Ambiente(dimensao_ambiente=5, t_pausa=0.0)\n    amb.mostrar_ambiente()\n    agente = AgenteReativoV1(amb)\n    p = agente.printw\n    while True:\n        agente.verificar_atirar_wumpus()\n        pos_mov = agente.sortear_pos(agente.get_opcoes_mov())\n        amb.atualiza_pos_agente(pos_mov)\n        amb.mostrar_ambiente()\n        agente.pegar_outro()\n        agente.status_agente_ouro()\n        agente.verificar_morte_agente_wumpus()\n        agente.verificar_morte_agente_poco()\n        if agente.verificar_vitorio():\n            passos += 1\n            rodadas += 1\n            agente.ganhou_jogo()\n            p(f"Qt. de passos no Ambiente: {passos}")\n            p(f"Qt. de rodadas: {rodadas}\\n")\n            os._exit(0)\n        elif agente.morreu:\n            break\n        passos += 1\n    p(f"Qt. de passos no Ambiente: {passos}")\n    rodadas += 1\n\n')),(0,n.kt)("p",null,(0,n.kt)("strong",{parentName:"p"},"Sa\xedda:")),(0,n.kt)("p",null,"Dependendo da quantidade de vezes que o agente morre, a sa\xedda pode ser extensa, abaixo \xe9 mostrado\nas \xfaltimas sa\xeddas para uma execu\xe7\xe3o do c\xf3digo."),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre"},".\n.\n.\n\nMundo do Wumpus:\n[[0 4 0 0 2]\n [0 0 0 0 2]\n [0 0 0 0 0]\n [2 0 0 0 2]\n [0 1 0 0 2]]\n[INFO:] O agente est\xe1 com o ouro!\n\nMundo do Wumpus:\n[[4 0 0 0 2]\n [0 0 0 0 2]\n [0 0 0 0 0]\n [2 0 0 0 2]\n [0 1 0 0 2]]\n[INFO:] O agente est\xe1 com o ouro!\n\n============== Fim de Jogo ==============\n          VIT\xd3RIA DO AGENTE\n=========================================\n\nQt. de passos no Ambiente: 8\nQt. de rodadas: 6\n\n")),(0,n.kt)("p",null,"Para que o ",(0,n.kt)("inlineCode",{parentName:"p"},"agente")," ven\xe7a a partida, ele deve pega o ouro e voltar para a posi\xe7\xe3o inicial ",(0,n.kt)("inlineCode",{parentName:"p"},"(0, 0)"),". Nessa execu\xe7\xe3o precisou de 12 partidas para que o agente vencesse o jogo."))}u.isMDXComponent=!0}}]);