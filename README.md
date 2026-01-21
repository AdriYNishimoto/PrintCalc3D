# Manual de Uso - PrintProfitCalc 3D

## 📋 Índice
1. [Instalação](#instalação)
2. [Primeiro Acesso](#primeiro-acesso)
3. [Como Usar](#como-usar)
4. [Configurações](#configurações)
5. [Histórico](#histórico)
6. [Dicas e Boas Práticas](#dicas-e-boas-práticas)

---

## 🚀 Instalação

### Opção 1: Executável (Recomendado)
1. Localize o arquivo `PrintProfitCalc3D.exe` na pasta `dist`
2. Copie o arquivo para o local desejado no computador
3. Execute o arquivo clicando duas vezes
4. **Importante**: Na primeira execução, o Windows pode exibir um aviso de segurança. Clique em "Mais informações" e depois em "Executar assim mesmo"

### Opção 2: Executar via Python
1. Certifique-se de ter Python 3.9+ instalado
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o aplicativo:
   ```bash
   python main.py
   ```

---

## 🎯 Primeiro Acesso

### Configuração Inicial
Ao abrir o aplicativo pela primeira vez, siga estes passos:

1. **Vá para a aba "Configurações"**
2. **Configure sua impressora:**
   - **Consumo da Impressora**: Potência em Watts (ex: 350W)
   - **Tarifa de Energia**: Valor do kWh da sua região (ex: R$ 0,85)
   - **Manutenção Mensal**: Custo médio mensal de manutenção (ex: R$ 50,00)
   - **Preço da Impressora**: Valor total pago pela impressora (ex: R$ 2.500,00)
   - **Vida Útil**: Estimativa de peças que a impressora produzirá (ex: 2000 peças)

3. **Configure os valores padrão:**
   - **Preço Padrão do Rolo**: Valor médio do filamento (ex: R$ 120,00)
   - **Peso Padrão do Rolo**: Peso do rolo em gramas (ex: 1000g)
   - **Valor Padrão da Hora**: Quanto você cobra por hora de trabalho (ex: R$ 30,00)
   - **Margem de Lucro Padrão**: Percentual de lucro desejado (ex: 50%)

4. **Clique em "SALVAR CONFIGURAÇÕES"**

---

## 💡 Como Usar

### Dashboard - Calculando o Custo de uma Peça

#### 1. Material
- **Preço do Rolo**: Quanto você pagou pelo rolo de filamento
- **Peso do Rolo**: Peso total do rolo (geralmente 1kg = 1000g)
- **Peso da Peça**: Peso que o slicer informou para a peça (em gramas)

#### 2. Tempo e Energia
- **Tempo de Impressão**: Horas que o slicer estimou
- **Consumo da Impressora**: Potência da impressora em Watts
- **Tarifa de Energia**: Custo do kWh na sua região

#### 3. Mão de Obra
- **Valor da Hora**: Quanto você cobra por hora de trabalho
- **Tempo de Prep/Pós**: Tempo gasto preparando a impressão e fazendo acabamento

#### 4. Impressora e Manutenção
- **Manutenção Mensal**: Custo mensal com manutenção
- **Est. Impressões Mensais**: Quantas peças você imprime por mês
- **Preço da Impressora**: Valor total da impressora
- **Vida Útil**: Quantas peças a impressora produzirá até precisar ser substituída

#### 5. Adicionais e Lucro
- **Custos Adicionais**: Embalagem, frete, etc.
- **Margem de Lucro**: Percentual de lucro desejado

#### 6. Calcular
1. Preencha todos os campos necessários
2. Clique em **"CALCULAR"**
3. O resultado aparecerá à direita com:
   - Custo de Filamento
   - Custo de Energia
   - Mão de Obra
   - Manutenção
   - Amortização
   - **Custo Total**
   - **Preço Sugerido** (com lucro)

4. Se desejar salvar, clique em **"SALVAR NO HISTÓRICO"**

---

## ⚙️ Configurações

### Quando Alterar as Configurações?
- Mudou de impressora
- Tarifa de energia foi reajustada
- Mudou o preço médio do filamento
- Quer ajustar a margem de lucro padrão

### Como Alterar
1. Vá para a aba **"Configurações"**
2. Modifique os valores desejados
3. Clique em **"SALVAR CONFIGURAÇÕES"**
4. As novas configurações serão aplicadas automaticamente no Dashboard

---

## 📊 Histórico

### Visualizar Cálculos Anteriores
1. Vá para a aba **"Histórico"**
2. Veja todos os cálculos salvos em formato de tabela
3. Informações exibidas:
   - Data e hora do cálculo
   - Peso da peça
   - Custo total
   - Preço sugerido
   - Tempo de impressão

### Exportar para Excel/CSV
1. Na aba **"Histórico"**, clique em **"Exportar para CSV"**
2. Escolha onde salvar o arquivo
3. Abra o arquivo no Excel, Google Sheets ou outro programa de planilhas

### Atualizar Histórico
- Clique em **"Atualizar"** para recarregar os dados

---

## 💎 Dicas e Boas Práticas

### Para Cálculos Mais Precisos

1. **Pese suas peças reais**: Use uma balança de precisão para confirmar o peso real após a impressão

2. **Monitore o consumo real**: Use um medidor de energia para verificar o consumo real da sua impressora

3. **Atualize a vida útil**: Revise periodicamente a estimativa de vida útil da impressora

4. **Considere todos os custos**: Não esqueça de incluir:
   - Embalagem
   - Etiquetas
   - Frete (se aplicável)
   - Falhas de impressão (adicione 5-10% no custo)

5. **Revise a margem de lucro**: Pesquise o mercado e ajuste sua margem conforme a concorrência

### Organização

1. **Salve sempre**: Salve cada cálculo no histórico para referência futura

2. **Exporte mensalmente**: Faça backup do histórico exportando para CSV todo mês

3. **Documente mudanças**: Anote quando alterar configurações importantes

### Precificação Inteligente

- **Margem mínima recomendada**: 30-50% para cobrir imprevistos
- **Margem para peças complexas**: 50-100% devido ao maior risco e tempo
- **Margem para grandes volumes**: Pode ser reduzida (20-30%) para clientes recorrentes

---

## ❓ Perguntas Frequentes

### O aplicativo não abre
- Verifique se o antivírus não está bloqueando
- Tente executar como administrador (botão direito → "Executar como administrador")

### Os cálculos parecem errados
- Verifique se todas as configurações estão corretas
- Confirme que está usando as unidades corretas (gramas, horas, Watts)
- Revise os valores padrão na aba Configurações

### Como calcular a vida útil da impressora?
- Exemplo: Se sua impressora custou R$ 2.500 e você espera que dure 2 anos imprimindo 100 peças/mês:
  - Vida útil = 2 anos × 12 meses × 100 peças = 2.400 peças

### Posso usar em várias máquinas?
- Sim! Basta copiar o arquivo `PrintProfitCalc3D.exe` para cada computador
- Cada máquina terá suas próprias configurações e histórico

---

## 📞 Suporte

Para dúvidas ou sugestões sobre o aplicativo, entre em contato com o desenvolvedor.

**Versão**: 1.0  
**Última atualização**: Novembro 2025
