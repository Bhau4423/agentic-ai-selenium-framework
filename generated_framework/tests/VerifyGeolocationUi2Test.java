package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.GeolocationPage;

public class VerifyGeolocationUi2Test extends BaseTest {

    @Test
    public void verifyGeolocationUi2() {

        GeolocationPage page = new GeolocationPage(driver);

        wait.until(ExpectedConditions.elementToBeClickable(page.get_Where_am_I?()));

        Assert.assertTrue(driver.getCurrentUrl().length() > 0);

    }

}