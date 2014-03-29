//
//  ALogController.h
//  ActivityLogger
//
//  Created by David Arnold on 29/03/14.
//  Copyright (c) 2014 David Arnold. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface ALogController : NSObject {
    IBOutlet NSComboBox *comboBox;
    IBOutlet NSWindow *taskWindow;
}

- (IBAction)ok:(id) sender;
- (IBAction)cancel:(id) sender;
@end
