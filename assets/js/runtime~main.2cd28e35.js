(()=>{"use strict";var e,a,f,t,r,c={},b={};function d(e){var a=b[e];if(void 0!==a)return a.exports;var f=b[e]={id:e,loaded:!1,exports:{}};return c[e].call(f.exports,f,f.exports,d),f.loaded=!0,f.exports}d.m=c,d.c=b,e=[],d.O=(a,f,t,r)=>{if(!f){var c=1/0;for(i=0;i<e.length;i++){f=e[i][0],t=e[i][1],r=e[i][2];for(var b=!0,o=0;o<f.length;o++)(!1&r||c>=r)&&Object.keys(d.O).every((e=>d.O[e](f[o])))?f.splice(o--,1):(b=!1,r<c&&(c=r));if(b){e.splice(i--,1);var n=t();void 0!==n&&(a=n)}}return a}r=r||0;for(var i=e.length;i>0&&e[i-1][2]>r;i--)e[i]=e[i-1];e[i]=[f,t,r]},d.n=e=>{var a=e&&e.__esModule?()=>e.default:()=>e;return d.d(a,{a:a}),a},f=Object.getPrototypeOf?e=>Object.getPrototypeOf(e):e=>e.__proto__,d.t=function(e,t){if(1&t&&(e=this(e)),8&t)return e;if("object"==typeof e&&e){if(4&t&&e.__esModule)return e;if(16&t&&"function"==typeof e.then)return e}var r=Object.create(null);d.r(r);var c={};a=a||[null,f({}),f([]),f(f)];for(var b=2&t&&e;"object"==typeof b&&!~a.indexOf(b);b=f(b))Object.getOwnPropertyNames(b).forEach((a=>c[a]=()=>e[a]));return c.default=()=>e,d.d(r,c),r},d.d=(e,a)=>{for(var f in a)d.o(a,f)&&!d.o(e,f)&&Object.defineProperty(e,f,{enumerable:!0,get:a[f]})},d.f={},d.e=e=>Promise.all(Object.keys(d.f).reduce(((a,f)=>(d.f[f](e,a),a)),[])),d.u=e=>"assets/js/"+({53:"935f2afb",734:"64d34e84",796:"76c1d1e0",948:"8717b14a",1154:"920172fa",1248:"ace85961",1302:"be048ad6",1318:"0e66ac20",1376:"d3326f77",1644:"e39bd66a",1914:"d9f32620",2058:"da168543",2267:"59362658",2362:"e273c56f",2535:"814f3328",2897:"776bf1e1",3080:"692b002c",3085:"1f391b9e",3089:"a6aa9e1f",3514:"73664a40",3608:"9e4087bc",3721:"5d0a2cba",4013:"01a85c17",4194:"4e0a7fe4",4195:"c4f5d8e4",4264:"28f6db54",4879:"24c94a27",4958:"6be31d28",5205:"130a244e",5357:"ec94ba56",5474:"6385fee8",5590:"062ebf8c",5831:"4536cb8e",5968:"9800b255",6001:"4ba2759b",6103:"ccc49370",6817:"6fcc6f82",7414:"393be207",7662:"bbacd35d",7918:"17896441",7975:"3ecd4b72",8020:"b7c58ec0",8380:"feed43a0",8610:"6875c492",8636:"f4f34a3a",9003:"925b3f96",9131:"bdef2f21",9514:"1be78505",9597:"6cd6aafe",9642:"7661071f",9671:"0e384e19",9817:"14eb3368",9839:"fe15a566"}[e]||e)+"."+{53:"c1ebc1b8",210:"dc26a667",734:"cb1dfeb2",796:"f801af9e",948:"c6b35957",1154:"f91f0c1d",1248:"bc7cd911",1302:"8c17294e",1318:"6ed489cf",1376:"354c0533",1644:"cdae76ae",1914:"025d8fb6",2058:"e1b4588a",2267:"e07b455d",2362:"26ff0dae",2529:"1ce48737",2535:"b4cc152c",2897:"b6c91075",3080:"23924be1",3085:"0571800e",3089:"845cad8c",3514:"7f2f5f88",3608:"064ee4cb",3721:"525f9b6b",4013:"44f4b362",4194:"c8416900",4195:"8547463e",4264:"48ea2dcb",4879:"8da81f1c",4958:"1bc7ae7b",4972:"96c55074",5205:"a47bfe7d",5357:"e316d3ef",5474:"2a9e8dea",5590:"84707507",5831:"d23523e1",5968:"8039e4e1",6001:"7ab643ca",6103:"d9c41d1e",6817:"3d41fe21",7414:"0967ba00",7662:"8c61f787",7918:"2b4fe47e",7975:"3ab6489b",8020:"7314c40f",8380:"25d61dbf",8610:"f37b7b5c",8636:"76ff6078",9003:"2e437d00",9131:"cb4b8d98",9514:"44076c16",9597:"b9c30c97",9642:"81af8e60",9671:"e745b718",9817:"1627c0d9",9839:"eec40cce"}[e]+".js",d.miniCssF=e=>{},d.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"==typeof window)return window}}(),d.o=(e,a)=>Object.prototype.hasOwnProperty.call(e,a),t={},r="docs:",d.l=(e,a,f,c)=>{if(t[e])t[e].push(a);else{var b,o;if(void 0!==f)for(var n=document.getElementsByTagName("script"),i=0;i<n.length;i++){var u=n[i];if(u.getAttribute("src")==e||u.getAttribute("data-webpack")==r+f){b=u;break}}b||(o=!0,(b=document.createElement("script")).charset="utf-8",b.timeout=120,d.nc&&b.setAttribute("nonce",d.nc),b.setAttribute("data-webpack",r+f),b.src=e),t[e]=[a];var l=(a,f)=>{b.onerror=b.onload=null,clearTimeout(s);var r=t[e];if(delete t[e],b.parentNode&&b.parentNode.removeChild(b),r&&r.forEach((e=>e(f))),a)return a(f)},s=setTimeout(l.bind(null,void 0,{type:"timeout",target:b}),12e4);b.onerror=l.bind(null,b.onerror),b.onload=l.bind(null,b.onload),o&&document.head.appendChild(b)}},d.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},d.p="/IA_mundo_do_wumpus/",d.gca=function(e){return e={17896441:"7918",59362658:"2267","935f2afb":"53","64d34e84":"734","76c1d1e0":"796","8717b14a":"948","920172fa":"1154",ace85961:"1248",be048ad6:"1302","0e66ac20":"1318",d3326f77:"1376",e39bd66a:"1644",d9f32620:"1914",da168543:"2058",e273c56f:"2362","814f3328":"2535","776bf1e1":"2897","692b002c":"3080","1f391b9e":"3085",a6aa9e1f:"3089","73664a40":"3514","9e4087bc":"3608","5d0a2cba":"3721","01a85c17":"4013","4e0a7fe4":"4194",c4f5d8e4:"4195","28f6db54":"4264","24c94a27":"4879","6be31d28":"4958","130a244e":"5205",ec94ba56:"5357","6385fee8":"5474","062ebf8c":"5590","4536cb8e":"5831","9800b255":"5968","4ba2759b":"6001",ccc49370:"6103","6fcc6f82":"6817","393be207":"7414",bbacd35d:"7662","3ecd4b72":"7975",b7c58ec0:"8020",feed43a0:"8380","6875c492":"8610",f4f34a3a:"8636","925b3f96":"9003",bdef2f21:"9131","1be78505":"9514","6cd6aafe":"9597","7661071f":"9642","0e384e19":"9671","14eb3368":"9817",fe15a566:"9839"}[e]||e,d.p+d.u(e)},(()=>{var e={1303:0,532:0};d.f.j=(a,f)=>{var t=d.o(e,a)?e[a]:void 0;if(0!==t)if(t)f.push(t[2]);else if(/^(1303|532)$/.test(a))e[a]=0;else{var r=new Promise(((f,r)=>t=e[a]=[f,r]));f.push(t[2]=r);var c=d.p+d.u(a),b=new Error;d.l(c,(f=>{if(d.o(e,a)&&(0!==(t=e[a])&&(e[a]=void 0),t)){var r=f&&("load"===f.type?"missing":f.type),c=f&&f.target&&f.target.src;b.message="Loading chunk "+a+" failed.\n("+r+": "+c+")",b.name="ChunkLoadError",b.type=r,b.request=c,t[1](b)}}),"chunk-"+a,a)}},d.O.j=a=>0===e[a];var a=(a,f)=>{var t,r,c=f[0],b=f[1],o=f[2],n=0;if(c.some((a=>0!==e[a]))){for(t in b)d.o(b,t)&&(d.m[t]=b[t]);if(o)var i=o(d)}for(a&&a(f);n<c.length;n++)r=c[n],d.o(e,r)&&e[r]&&e[r][0](),e[r]=0;return d.O(i)},f=self.webpackChunkdocs=self.webpackChunkdocs||[];f.forEach(a.bind(null,0)),f.push=a.bind(null,f.push.bind(f))})()})();