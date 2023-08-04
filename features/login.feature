Feature: Web Login
  Scenario: usuario ingresa sus credenciales
    Given usuario ingrea a la pagina demoguru
    When usuario da click en singon
    And usuario ingresa sus credenciales
    And click en submit
    Then logeo exitoso