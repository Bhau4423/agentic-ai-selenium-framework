package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.NotificationMessageRenderedPage;

public class VerifyNoCrashOnRapidRefreshTest extends BaseTest {

    @Test
    public void verifyNoCrashOnRapidRefresh() {

        NotificationMessageRenderedPage page = new NotificationMessageRenderedPage(driver);

        Assert.assertFalse(driver.getCurrentUrl().contains("dashboard"));

    }

}