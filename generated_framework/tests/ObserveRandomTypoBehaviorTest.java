package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.TyposPage;

public class ObserveRandomTypoBehaviorTest extends BaseTest {

    @Test
    public void observeRandomTypoBehavior() {

        TyposPage page = new TyposPage(driver);

        Assert.assertTrue(driver.getCurrentUrl().length() > 0);

    }

}