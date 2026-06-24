package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.NonExistentPage;

public class AccessNonExistentPageTest extends BaseTest {

    @Test
    public void accessNonExistentPage() {

        NonExistentPage page = new NonExistentPage(driver);

        Assert.assertFalse(driver.getCurrentUrl().contains("dashboard"));

    }

}