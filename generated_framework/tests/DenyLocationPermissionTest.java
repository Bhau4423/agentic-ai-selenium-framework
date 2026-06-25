package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.GeolocationPage;

public class DenyLocationPermissionTest extends BaseTest {

    @Test
    public void denyLocationPermission() {

        GeolocationPage page = new GeolocationPage(driver);

        wait.until(ExpectedConditions.elementToBeClickable(page.get_Where_am_I?()));
        page.get_Where_am_I_().click();

        wait.until(ExpectedConditions.visibilityOf(page.get_Where_am_I?()));
        // UNKNOWN ACTION : ALERT_DISMISS

        Assert.assertFalse(driver.getCurrentUrl().contains("dashboard"));

    }

}