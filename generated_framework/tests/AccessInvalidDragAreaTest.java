package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.NonExistentPage;

public class AccessInvalidDragAreaTest extends BaseTest {

    @Test
    public void accessInvalidDragArea() {

        NonExistentPage page = new NonExistentPage(driver);

        Assert.assertFalse(driver.getCurrentUrl().contains("dashboard"));

    }

}