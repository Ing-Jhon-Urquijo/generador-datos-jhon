package com.latam.test.stepdefinitions;

import com.latam.test.pages.SearchFlightPage;
import io.cucumber.java.en.When;
import net.serenitybdd.core.annotations.findby.By;
import net.thucydides.core.annotations.Managed;
import org.openqa.selenium.WebDriver;

public class SearchFlightStepDefinitions {

    @Managed
    WebDriver driver;

    SearchFlightPage searchFlightPage;

    @When("el usuario realiza una búsqueda de vuelo")
    public void el_usuario_realiza_una_busqueda() {
        driver.get("https://www.latamairlines.com/co/es");
        searchFlightPage.clickOnSearch();
    }
}
