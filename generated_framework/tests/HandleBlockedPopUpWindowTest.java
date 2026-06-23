package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.WindowsPage;

public class HandleBlockedPopUpWindowTest extends BaseTest {

    @Test
    public void handleBlockedPopUpWindow() {

        WindowsPage page = new WindowsPage(driver);

        Assert.assertFalse(driver.getCurrentUrl().contains("dashboard"));

    }

}