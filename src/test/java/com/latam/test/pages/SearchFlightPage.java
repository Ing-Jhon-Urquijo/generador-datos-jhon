package com.latam.test.pages;

import net.serenitybdd.core.pages.PageObject;
import net.serenitybdd.core.annotations.findby.FindBy;
import org.openqa.selenium.WebElement;

public class SearchFlightPage extends PageObject {

    @FindBy(id = "bookingSearch")
    WebElement bookingSearch;

    public void clickOnSearch() {
        bookingSearch.click();
    }
}
