package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.InputsPage;

public class EnterMaximumIntegerValueTest extends BaseTest {

    @Test
    public void enterMaximumIntegerValue() {

        InputsPage page = new InputsPage(driver);

        wait.until(ExpectedConditions.visibilityOf(page.get_input_0()));
        page.get_input_0().sendKeys("TEST_DATA");

        Assert.assertTrue(driver.getCurrentUrl().contains("dashboard"));

    }

}