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

        Assert.assertFalse(driver.getCurrentUrl().contains("dashboard"));

    }

}