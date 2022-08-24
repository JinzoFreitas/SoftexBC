# **Softex - Recife**

## **JavaScript**

## **Desenvolvimento 01**

## **Aluno:** Janderson Freitas

___

Acesse pelo menos dois sites de sua preferência e os inspecione com o botão direito do mouse na página web. Com o código fonte aberto você deve:
Verificar no código algum elemento que utilize JavaScript;
Marcar alguns elementos do site;
Explicar como ele se comporta. Exemplo: entrar no site do Google, inspecionar o botão de pesquisa, verificar o código e explicar qual a finalidade do botão.
___

**Resposta:**

Foi utilizado como exemplo 1 o site: <https://www.w3schools.com/>

Ao clicar no link `<a>` do HTML da página, a propriedade `onclick` chama a função `w3_open()` do javascript, que por sua vez seleciona itens do menu html e muda sua propriedade 'display', atualizando para 'none', caso esteja 'inline', e para 'inline', caso esteja 'none'.
Tornando assim o item visível ou invisível para o usuário.

```HTML
<!-- Parte do código em HTML -->

<a class="w3-bar-item w3-button bar-item-hover w3-padding-24" href="javascript:void(0)" onclick="w3_open()" id="navbtn_menu" title="Menu" style="width:93px">Menu <i class='fa fa-caret-down'></i><i class='fa fa-caret-up' style="display:none"></i></a>
```

```javascript
/* Parte do código em JavaScript */

function w3_open() {
  var x = document.getElementById("myAccordion");
  if (x.style.display === 'none') {
    x.style.display = 'block';
    if (document.getElementById("navbtn_menu")) {
      document.getElementById("navbtn_menu").getElementsByTagName("i")[0].style.display = "none";
      document.getElementById("navbtn_menu").getElementsByTagName("i")[1].style.display = "inline";
    }
  } else {
    x.style.display = 'none';
    if (document.getElementById("navbtn_menu")) {
      document.getElementById("navbtn_menu").getElementsByTagName("i")[0].style.display = "inline";
      document.getElementById("navbtn_menu").getElementsByTagName("i")[1].style.display = "none";
    }
  }
}
```

Foi utilizado como exemplo 2 o site: <https://vangoghgallery.com/>

Ao clicar na tag `<span>` do HTML da página, a propriedade `onclick` chama a função `openNav()` do javascript, que por sua vez seleciona o iten do html com o ID "mySidenav" e muda sua propriedade 'width', atualizando para '300px'

Tornando assim o item visível o usuário.

```HTML
<!-- Parte do código em HTML -->

<span class="hidden-lg hidden-sm hidden-md hidden-xl hidden-lg" onclick="openNav()" onkeypress="openNav()"></span>
```

```javascript
/* Parte do código em JavaScript */

function openNav() {
  document.getElementById("mySidenav").style.width = "300px";
}

/* Set the width of the side navigation to 0 */

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  }
```