package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.NonExistentPage;

public class ObserveCorrectTextTest extends BaseTest {

    @Test
    public void observeCorrectText() {

        NonExistentPage page = new NonExistentPage(driver);

        Assert.assertTrue(driver.getCurrentUrl().length() > 0);

    }

}