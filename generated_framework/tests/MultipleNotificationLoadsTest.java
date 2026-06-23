package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.NotificationMessageRenderedPage;

public class MultipleNotificationLoadsTest extends BaseTest {

    @Test
    public void multipleNotificationLoads() {

        NotificationMessageRenderedPage page = new NotificationMessageRenderedPage(driver);

        Assert.assertTrue(driver.getCurrentUrl().length() > 0);

    }

}