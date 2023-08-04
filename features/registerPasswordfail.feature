Feature: usuario se registra en la pagina DemoGuru
  Scenario: un nuevo usuario se registra en DemoGuru e ingresa dos contraseñas diferentes
    Given usuario ingrea a la pagina demoguru
    When click en register
    And usuario ingresa dos contraseñas diferentes
    And click en enviar
    Then permanece en la pagina de registro