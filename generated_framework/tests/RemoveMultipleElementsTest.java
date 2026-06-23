package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.AddRemoveElementsPage;

public class RemoveMultipleElementsTest extends BaseTest {

    @Test
    public void removeMultipleElements() {

        AddRemoveElementsPage page = new AddRemoveElementsPage(driver);


        Assert.assertTrue(driver.getCurrentUrl().length() > 0);

    }

}