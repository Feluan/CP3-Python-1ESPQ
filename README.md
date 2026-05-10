<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>JOVI Academy - Controle de Avaliações</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #0d1117;
      color: #e6edf3;
      margin: 40px;
    }

    h1, h2 {
      color: #58a6ff;
    }

    .card {
      background-color: #161b22;
      padding: 20px;
      border-radius: 12px;
      margin-bottom: 20px;
      box-shadow: 0 0 10px rgba(0,0,0,0.3);
    }

    ul {
      margin-left: 20px;
    }

    li {
      margin-bottom: 8px;
    }

    code {
      background-color: #21262d;
      padding: 4px 8px;
      border-radius: 6px;
      color: #79c0ff;
    }

    .emoji {
      font-size: 1.2em;
      margin-right: 6px;
    }
  </style>
</head>
<body>

  <h1>📸 JOVI Academy - Controle de Avaliações</h1>

  <div class="card">
    <h2>🧠 Sobre o Programa</h2>
    <p>
      Este programa simula um sistema da câmera <strong>JOVI Academy Mode</strong>,
      responsável por registrar avaliações de qualidade de tradução (de 0 a 100).
    </p>
    <p>
      O usuário insere várias notas, que são armazenadas em uma lista.
      Ao final, o sistema processa essas informações e gera um relatório contendo:
    </p>
    <ul>
      <li>📊 Média das avaliações</li>
      <li>🔢 Quantidade total de registros</li>
      <li>⭐ Desempenho geral das traduções</li>
    </ul>
  </div>

  <div class="card">
    <h2>⚙️ Funcionalidades Utilizadas</h2>

    <h3>⌨️ Entrada de Dados</h3>
    <p><code>input()</code> → Permite que o usuário digite as avaliações diretamente no terminal.</p>

    <h3>📥 Armazenamento</h3>
    <p><code>append()</code> → Adiciona cada nova nota na lista <code>avaliacoes</code>.</p>

    <h3>📊 Processamento de Dados</h3>
    <ul>
      <li><code>len()</code> → Retorna a quantidade de avaliações registradas.</li>
      <li><code>sum()</code> → Soma todas as notas da lista para calcular a média.</li>
      <li><code>for</code> → Percorre os valores para análises (ex: notas ≥ 80).</li>
    </ul>

    <h3>📈 Organização dos Resultados</h3>
    <p><code>sort()</code> → Ordena as avaliações em ordem decrescente.</p>
  </div>

  <div class="card">
    <h2>🚀 Resultado Final</h2>
    <p>
      Ao executar o programa, o usuário recebe um relatório completo no terminal,
      simulando o funcionamento de análise de desempenho da câmera JOVI.
    </p>
  </div>


</body>
</html>
