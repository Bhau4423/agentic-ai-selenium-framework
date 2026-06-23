package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.DropdownPage;

public class InvalidSelectionAttemptTest extends BaseTest {

    @Test
    public void invalidSelectionAttempt() {

        DropdownPage page = new DropdownPage(driver);

        wait.until(ExpectedConditions.visibilityOf(page.get_dropdown()));
        // TODO: Select value for dropdown

        wait.until(ExpectedConditions.visibilityOf(page.get_dropdown()));
        Assert.assertFalse(driver.getCurrentUrl().contains("dashboard"));

    }

}