package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.InputsPage;

public class EnterNonNumericDataTest extends BaseTest {

    @Test
    public void enterNonNumericData() {

        InputsPage page = new InputsPage(driver);


        Assert.assertFalse(driver.getCurrentUrl().contains("dashboard"));

    }

}