Feature: usuario se registra en la pagina DemoGuru
  Scenario: un nuevo usuario se registra en DemoGuru y no ingresa los datos en los campos obligatorios
    Given usuario ingrea a la pagina demoguru
    When click en register
    When usuario no ingresa los campos obligatorios
    And click en enviar
    Then permanece en la pagina de registro