Feature: usuario se registra en la pagina DemoGuru
  Scenario: un nuevo usuario se registra en DemoGuru
    Given usuario ingrea a la pagina demoguru
    When click en register
    And usuario ingresa sus datos
    And click en enviar
    Then registro exitoso