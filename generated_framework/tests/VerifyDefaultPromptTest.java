package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.DropdownPage;

public class VerifyDefaultPromptTest extends BaseTest {

    @Test
    public void verifyDefaultPrompt() {

        DropdownPage page = new DropdownPage(driver);

        wait.until(ExpectedConditions.visibilityOf(page.get_dropdown()));
        Assert.assertTrue(driver.getCurrentUrl().contains("dashboard"));

    }

}