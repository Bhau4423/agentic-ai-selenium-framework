package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.InputsPage;

public class IncrementValueAtBoundaryTest extends BaseTest {

    @Test
    public void incrementValueAtBoundary() {

        InputsPage page = new InputsPage(driver);

        wait.until(ExpectedConditions.visibilityOf(page.get_input_0()));
        page.get_input_0().sendKeys("TEST_DATA");

        wait.until(ExpectedConditions.elementToBeClickable(page.get_input_0()));
        page.get_input_0().click();

        wait.until(ExpectedConditions.visibilityOf(page.get_input_0()));
        Assert.assertTrue(driver.getCurrentUrl().contains("dashboard"));

    }

}