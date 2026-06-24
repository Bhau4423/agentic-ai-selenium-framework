package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.CheckboxesPage;

public class VerifyFooterVisibilityOnSmallScreenTest extends BaseTest {

    @Test
    public void verifyFooterVisibilityOnSmallScreen() {

        CheckboxesPage page = new CheckboxesPage(driver);

        Assert.assertTrue(driver.getCurrentUrl().contains("dashboard"));

    }

}